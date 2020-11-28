API Examples
============


Users API
---------

.. code-block:: python

    from pyokapi.folio.api.users import Users
    
    tenant = "mylib"
    usersApi = Users(tenant)
    
    # Get all users
    users = usersApi.get_users()
    
    # Make a cql query for the folio_admin user
    users = usersApi.get_users(query="username==folio_admin")

There are also methods, that combins API calls.

.. code-block:: python





Inventory API
-------------

.. code-block:: python

    from pyokapi.folio.api.inventory import Inventory
    from pyokapi.folio.api.inventoryStorage import InstanceStorage

    tenant = "mylib"
    instanceStorageApi = InstanceStorage(tenant)
    inventoryApi = Inventory(tenant)
    
    # Get all instances
    instanceStorageApi.get_instances()

    # Get all items
    items = inventoryApi.get_items()


    
    
    