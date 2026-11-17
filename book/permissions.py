from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # წიგნების ნახვა ყველას შეუძლია
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # წიგნის დამატება ყველას შეუძლია
        if request.method == 'POST':
            return request.user.is_authenticated

        # განახლება და წაშლა მხოლოდ ადმინისტრატორს
        return request.user.is_staff