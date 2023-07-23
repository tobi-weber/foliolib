CLI Reference
=============

.. code-block:: bash

    foliolib --help


- **okapi**

    Commands to manage okapi.

  - **version**

      Get Okapi version.

  - **health**

      Get health.

  - **nodes**

      List Nodes.

  - **env**

      List global enviroment variables.

  - **add-env**

      Add global enviroment variable.

  - **del-env**

      Remove global enviroment variable.

  - **secure**

      Secure Okapi installation.

  - **unsecure**

      Unsecure Okapi installation.

  - **clean**

      undeploy and remove not enabled modules in any tenant.


- **module**

    Commands to manage Modules.

  - **lst**

      List modules.

  - **get**

      Get ModulDescriptor.

  - **add**

      Add module(s) by id.

  - **addmd**

      Add ModulDescriptor(s).

  - **remove**

      Remove module(s).

  - **deployed**

      List deployed modules.

  - **deploy**

      Deploy module(s) for a node.

  - **undeploy**

      Undeploy module(s).


- **tenant**

    Commands to manage tenants.

  - **lst**

      List tenants.

  - **add**

      Add new tenant.

  - **remove**

      Remove tenant.

  - **modify**

      Modify tenant.

  - **enable**

      Enable module(s) for a tenant.

  - **disable**

      Disable module(s) for a tenant.

  - **upgrade**

      Upgrade tenant.

  - **upgrademodule**

      Upgrade  module(s) for a tenant.

  - **modules**

      List modules of a tenant.

  - **interfaces**

      List interface(s).

  - **uninstall**

      Disable all modules of a tenant and remove the tenant.


- **platform**

    Commands to install and upgraede Folio platform.

  - **install**

      Install a folio platform.
      This can be called multiple times, to setup different tenants.

  - **upgrade**

      Upgrade folio tenants.
      It is recommended to unsecure Okapi before upgrading.
      It may be necessary to update Okapi before upgrading.


- **folio**

    Commands to manage Folio.

  - **login**

      Log in a tenant.

  - **superuser**

      Create superuser for a tenant.

  - **inventory**

      Commands related to inventory.

      - **loadref**

        Load referencedata from filesystem path.

      - **dumpref**

        Write referencedata to filesystem path.

      - **reindex**

        Create indicies if needed and reindex.

      - **totals**

        Show total records in inventory.
  
  - **config**

      Commands related to config.

      - **lst**

        List config entries.

  - **email**

      Commands related to email config.

      - **get**

        Get EMail config.

      - **set**

        Set EMail config.

      - **delete**

        Delete EMail config.

  - **foliohost**

      Commands related to email config.

      - **get**

        Get Folio UI application host.

      - **set**

        Set Folio UI application host.

      - **delete**

        Delete Folio UI application host.

- **server**

    Commands to manage foliolib server configs.

  - **active**

      Show active server.

  - **lst**

      List available server configs.

  - **enable**

      Enable server config.

  - **create**

      Create new server config.

  - **delete**

      Delete a server config.


- **loginokapi**

    Login into Okapi. Only available, if a authentication for
    the supertenant is required.
