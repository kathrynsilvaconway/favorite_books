from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('process_reg', views.process_reg),
    path('process_login', views.process_login),
    path('books', views.render_home),
    path('log_out', views.log_out),
    path('upload_book', views.upload_book),
    path('display_book/<int:this_book_id>', views.display_book),
    path('delete_book/<int:this_book_id>', views.delete_book),
    path('update_book/<int:this_book_id>', views.update_book),
    path('add_to_likes/<int:this_book_id>', views.add_to_likes),
    path('remove_like/<int:this_book_id>', views.remove_like),
    path('user_favorites/<int:this_user_id>', views.user_favorites)
    
]
