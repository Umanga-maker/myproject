
from rest_framework.permissions import BasePermission
SUPER_ADMIN=1
ADMIN=2
def IsAuthenticated(request):
    return  bool(request.user and request.user.is_authenticated)
def SuperAdminLevel(request):
    return  bool(request.user and request.user.is_superuser)
def AdminLevrl(request):
    return  bool(request.user and request.user.role in [ADMIN])

def IsOwner(request):
    if str(request.user.id)==str(request.data.get('user')):
        return True
    elif len(request.data)==0 and len(request.POST)==0:
        return True
    return False 

class RefPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['List']:
            return True
        elif view.action in ['retrieve']:
            return IsOwner(request)
        elif view.action in ['create','update']:
            return IsOwner(request)
        elif view.action == 'partial_update':
            return IsOwner(request)
        elif view.action =='destroy':
            return IsOwner(request)
