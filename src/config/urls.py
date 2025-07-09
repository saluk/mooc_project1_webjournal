"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

import time

class MyAuthenticationForm(AuthenticationForm):
    fail_cache = {}
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
    def confirm_login_allowed(self, user):
        fail = self.fail_cache.get(user.get_username(), {})
        if fail and fail["fail"] > 3 and time.time()-fail["lastfail"] < 5*60:
            raise ValidationError(
                self.error_messages["invalid_login"],
                code="invalid_login",
                params={"username": self.username_field.verbose_name},
            )
        return super().confirm_login_allowed(user)
    def get_invalid_login_error(self):
        username = self.cleaned_data.get("username")
        ### OWASP A07 - Uncomment to add a 5 minute timeout for a user if they submit a failed password too many times ###
        # if not username in self.fail_cache:
        #     self.fail_cache[username] = {"fail": 0, "lastfail": 0}
        # self.fail_cache[username]["fail"] += 1
        # self.fail_cache[username]["lastfail"] = time.time()

        ### OWASP A09 - Uncomment to log the failed login
        # print(f"Alert! Failed login for {username}")
        return super().get_invalid_login_error()

class MyLoginView(LoginView):
    authentication_form = MyAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', MyLoginView.as_view(template_name='pages/login.html')),
	path('logout/', LogoutView.as_view(next_page='/')),
	path('', include('src.pages.urls'))
]
