from .category_urls import urlpatterns as category_urls
from .post_urls import urlpatterns as post_urls
from .user_urls import urlpatterns as user_urls
from .gender_urls import urlpatterns as gender_urls
from .province_urls import urlpatterns as province_urls
from .status_urls import urlpatterns as status_urls
from .token_urls import urlpatterns as token_urls

urlpatterns = category_urls + post_urls + user_urls + gender_urls + province_urls + status_urls + token_urls
