from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from accounts.forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    '''サインアップページのビュー

    '''
    # form.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    #レンダリングするテンプレート
    template_name = "accounts/signup.html"
    #サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('signup_success')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる *バリデーション（認証の通過)
        ファームデータの登録をおこなう

        '''

        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        #　戻り値はスーパークラスのform_valid()の戻り値（HttpResponseRedirect)
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):

    template_name = "accounts/signup_success.html"