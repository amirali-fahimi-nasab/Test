
from rest_framework import routers

from .views import BlogViews


router = routers.SimpleRouter()
router.register('blog', BlogViews , basename = 'blogs')
urlpatterns = router.urls
