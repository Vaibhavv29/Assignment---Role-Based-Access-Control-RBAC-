// Define Roles and Permissions 

roles = {
    'Admin': {'create', 'read', 'update', 'delete'},
    'Editor': {'create', 'read', 'update'},
    'Viewer': {'read'},
}

// Check User Role Permissions

def has_permission(role, action):
    return action in roles.get(role, set())


user_role = 'Editor'

if has_permission(user_role, 'delete'):
    print("Permission granted.")
else:
    print("Access denied.")
