from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class UserAdminViewSet(ModelViewSet):
    """
    A viewset to provide general facility
    """
    model = None
    serializer_list = {
        'view':{
            'user':None, 
            'public': None,
            'admin': None,
        },
        'edit':{
            'user': None,
            'public': None,
            'admin': None,
        }
    }
    
    methods = {
        'user': ['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'],
        'public':['OPTIONS'], # add 'GET' method to allow viewing data to all
        'admin': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
    }

    def get_admin_serializer(self):
        if self.action == 'list' or self.action == 'retrieve':
            # got viewing 
            return self.serializer_list['view']['admin']
        #elif self.action == 'create':
        return self.serializer_list['edit']['admin']
        
    
    def get_user_serializer(self):
        if self.action == 'list' or self.action == 'retrieve':
            # got viewing 
            return self.serializer_list['view']['user']
        #elif self.action == 'create':
        return self.serializer_list['edit']['user']
        
    
    def get_public_serializer(self):
        if self.action == 'list' or self.action == 'retrieve':
            # got viewing 
            return self.serializer_list['view']['public']
        #elif self.action == 'create':
        return self.serializer_list['edit']['public']

    def get_serializer_class(self):
        serial = None
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                serial = self.get_admin_serializer()
            else:
                serial = self.get_user_serializer()
        else:
            serial = self.get_public_serializer()
        if serial == None:
            return self.serializer_class
        else:
            return serial
    
    def get_queryset(self):
        if self.model == None:
            return self.queryset
        else:
            if not self.request.user.is_authenticated:
                # public user ....
                if 'GET' in self.methods['public']:
                    # public is allowed to view data
                    return self.model.objects.all()
                else:
                    return self.model.objects.filter(pk=-1)
            elif self.request.user.is_staff:
                # if user parameter is passed, then go for that or show the default val
                x = self.request.GET.get("user", "")
                if x != "":
                    if x == "*":
                        return self.model.objects.all()
                    return self.model.objects.filter(user=x)

            # till now user must be authenticated
            return self.model.objects.filter(user=self.request.user)

            
