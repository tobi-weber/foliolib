# -*- coding: utf-8 -*-
# Generated at 2023-07-10

import logging

from foliolib.folio import FolioApi, FolioAdminApi

log = logging.getLogger("oliolib.folio.api.courses")


class Courses(FolioApi):
    """Course Reserves API

    API calls to perform CRUD on item reservations for courses
    """

    def get_courselistings(self, **kwargs):
        """Return a list of listings

        ``GET /coursereserves/courselistings``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_courselistings_return.schema 
        """
        return self.call("GET", "/coursereserves/courselistings", query=kwargs)

    def set_courselisting(self, courselisting: dict):
        """Create a new listing

        ``POST /coursereserves/courselistings``

        Args:
            courselisting (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created courselisting item

        Schema:

            .. literalinclude:: ../files/Courses_set_courselisting_request.schema
        """
        return self.call("POST", "/coursereserves/courselistings", data=courselisting)

    def delete_courselistings(self):
        """

        ``DELETE /coursereserves/courselistings``
        """
        return self.call("DELETE", "/coursereserves/courselistings")

    def get_courselisting(self, listing_id: str):
        """Retrieve courselisting item with given {courselistingId}

        ``GET /coursereserves/courselistings/{listing_id}``

        Args:
            listing_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_courselisting_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}")

    def delete_courselisting(self, listing_id: str):
        """Delete courselisting item with given {courselistingId}

        ``DELETE /coursereserves/courselistings/{listing_id}``

        Args:
            listing_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}")

    def modify_courselisting(self, listing_id: str, courselisting: dict):
        """Update a listing by id

        ``PUT /coursereserves/courselistings/{listing_id}``

        Args:
            listing_id (str)
            courselisting (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_courselisting_request.schema
        """
        return self.call("PUT", f"/coursereserves/courselistings/{listing_id}", data=courselisting)

    def get_instructors(self, listing_id: str, **kwargs):
        """Return a list of instructors

        ``GET /coursereserves/courselistings/{listing_id}/instructors``

        Args:
            listing_id (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_instructors_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/instructors", query=kwargs)

    def set_instructor(self, listing_id: str, instructor: dict):
        """Create a new instructor

        ``POST /coursereserves/courselistings/{listing_id}/instructors``

        Args:
            listing_id (str)
            instructor (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created instructor item

        Schema:

            .. literalinclude:: ../files/Courses_set_instructor_request.schema
        """
        return self.call("POST", f"/coursereserves/courselistings/{listing_id}/instructors", data=instructor)

    def delete_instructors(self, listing_id: str):
        """

        ``DELETE /coursereserves/courselistings/{listing_id}/instructors``

        Args:
            listing_id (str)
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/instructors")

    def get_instructor(self, listing_id: str, instructor_id: str):
        """Retrieve instructor item with given {instructorId}

        ``GET /coursereserves/courselistings/{listing_id}/instructors/{instructor_id}``

        Args:
            listing_id (str)
            instructor_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_instructor_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/instructors/{instructor_id}")

    def delete_instructor(self, listing_id: str, instructor_id: str):
        """Delete instructor item with given {instructorId}

        ``DELETE /coursereserves/courselistings/{listing_id}/instructors/{instructor_id}``

        Args:
            listing_id (str)
            instructor_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/instructors/{instructor_id}")

    def modify_instructor(self, listing_id: str, instructor_id: str, instructor: dict):
        """Update an instructor by id

        ``PUT /coursereserves/courselistings/{listing_id}/instructors/{instructor_id}``

        Args:
            listing_id (str)
            instructor_id (str)
            instructor (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_instructor_request.schema
        """
        return self.call("PUT", f"/coursereserves/courselistings/{listing_id}/instructors/{instructor_id}", data=instructor)

    def get_roles(self, **kwargs):
        """Return a list of roles

        ``GET /coursereserves/roles``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_roles_return.schema 
        """
        return self.call("GET", "/coursereserves/roles", query=kwargs)

    def set_role(self, role: dict):
        """Create a new role

        ``POST /coursereserves/roles``

        Args:
            role (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created role item

        Schema:

            .. literalinclude:: ../files/Courses_set_role_request.schema
        """
        return self.call("POST", "/coursereserves/roles", data=role)

    def delete_roles(self):
        """

        ``DELETE /coursereserves/roles``
        """
        return self.call("DELETE", "/coursereserves/roles")

    def get_role(self, role_id: str):
        """Retrieve role item with given {roleId}

        ``GET /coursereserves/roles/{role_id}``

        Args:
            role_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_role_return.schema 
        """
        return self.call("GET", f"/coursereserves/roles/{role_id}")

    def delete_role(self, role_id: str):
        """Delete role item with given {roleId}

        ``DELETE /coursereserves/roles/{role_id}``

        Args:
            role_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/roles/{role_id}")

    def modify_role(self, role_id: str, role: dict):
        """Update a role by id

        ``PUT /coursereserves/roles/{role_id}``

        Args:
            role_id (str)
            role (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_role_request.schema
        """
        return self.call("PUT", f"/coursereserves/roles/{role_id}", data=role)

    def get_terms(self, **kwargs):
        """Return a list of terms

        ``GET /coursereserves/terms``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_terms_return.schema 
        """
        return self.call("GET", "/coursereserves/terms", query=kwargs)

    def set_term(self, term: dict):
        """Create a new term

        ``POST /coursereserves/terms``

        Args:
            term (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created term item

        Schema:

            .. literalinclude:: ../files/Courses_set_term_request.schema
        """
        return self.call("POST", "/coursereserves/terms", data=term)

    def delete_terms(self):
        """

        ``DELETE /coursereserves/terms``
        """
        return self.call("DELETE", "/coursereserves/terms")

    def get_term(self, term_id: str):
        """Retrieve term item with given {termId}

        ``GET /coursereserves/terms/{term_id}``

        Args:
            term_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_term_return.schema 
        """
        return self.call("GET", f"/coursereserves/terms/{term_id}")

    def delete_term(self, term_id: str):
        """Delete term item with given {termId}

        ``DELETE /coursereserves/terms/{term_id}``

        Args:
            term_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/terms/{term_id}")

    def modify_term(self, term_id: str, term: dict):
        """Update a term by id

        ``PUT /coursereserves/terms/{term_id}``

        Args:
            term_id (str)
            term (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_term_request.schema
        """
        return self.call("PUT", f"/coursereserves/terms/{term_id}", data=term)

    def get_coursetypes(self, **kwargs):
        """Return a list of course types

        ``GET /coursereserves/coursetypes``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_coursetypes_return.schema 
        """
        return self.call("GET", "/coursereserves/coursetypes", query=kwargs)

    def set_coursetype(self, coursetype: dict):
        """Create a new course type

        ``POST /coursereserves/coursetypes``

        Args:
            coursetype (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created coursetype item

        Schema:

            .. literalinclude:: ../files/Courses_set_coursetype_request.schema
        """
        return self.call("POST", "/coursereserves/coursetypes", data=coursetype)

    def delete_coursetypes(self):
        """

        ``DELETE /coursereserves/coursetypes``
        """
        return self.call("DELETE", "/coursereserves/coursetypes")

    def get_coursetype(self, type_id: str):
        """Retrieve coursetype item with given {coursetypeId}

        ``GET /coursereserves/coursetypes/{type_id}``

        Args:
            type_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_coursetype_return.schema 
        """
        return self.call("GET", f"/coursereserves/coursetypes/{type_id}")

    def delete_coursetype(self, type_id: str):
        """Delete coursetype item with given {coursetypeId}

        ``DELETE /coursereserves/coursetypes/{type_id}``

        Args:
            type_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/coursetypes/{type_id}")

    def modify_coursetype(self, type_id: str, coursetype: dict):
        """Update a course type by id

        ``PUT /coursereserves/coursetypes/{type_id}``

        Args:
            type_id (str)
            coursetype (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_coursetype_request.schema
        """
        return self.call("PUT", f"/coursereserves/coursetypes/{type_id}", data=coursetype)

    def get_departments(self, **kwargs):
        """Return a list of departments

        ``GET /coursereserves/departments``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_departments_return.schema 
        """
        return self.call("GET", "/coursereserves/departments", query=kwargs)

    def set_department(self, department: dict):
        """Create a new department

        ``POST /coursereserves/departments``

        Args:
            department (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created department item

        Schema:

            .. literalinclude:: ../files/Courses_set_department_request.schema
        """
        return self.call("POST", "/coursereserves/departments", data=department)

    def delete_departments(self):
        """

        ``DELETE /coursereserves/departments``
        """
        return self.call("DELETE", "/coursereserves/departments")

    def get_department(self, department_id: str):
        """Retrieve department item with given {departmentId}

        ``GET /coursereserves/departments/{department_id}``

        Args:
            department_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_department_return.schema 
        """
        return self.call("GET", f"/coursereserves/departments/{department_id}")

    def delete_department(self, department_id: str):
        """Delete department item with given {departmentId}

        ``DELETE /coursereserves/departments/{department_id}``

        Args:
            department_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/departments/{department_id}")

    def modify_department(self, department_id: str, department: dict):
        """Update a department by id

        ``PUT /coursereserves/departments/{department_id}``

        Args:
            department_id (str)
            department (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_department_request.schema
        """
        return self.call("PUT", f"/coursereserves/departments/{department_id}", data=department)

    def get_processingstatuses(self, **kwargs):
        """Return a list of statuses

        ``GET /coursereserves/processingstatuses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_processingstatuses_return.schema 
        """
        return self.call("GET", "/coursereserves/processingstatuses", query=kwargs)

    def set_processingstatus(self, processingstatus: dict):
        """Create a new status

        ``POST /coursereserves/processingstatuses``

        Args:
            processingstatus (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created processingstatus item

        Schema:

            .. literalinclude:: ../files/Courses_set_processingstatus_request.schema
        """
        return self.call("POST", "/coursereserves/processingstatuses", data=processingstatus)

    def delete_processingstatuses(self):
        """

        ``DELETE /coursereserves/processingstatuses``
        """
        return self.call("DELETE", "/coursereserves/processingstatuses")

    def get_processingstatus(self, status_id: str):
        """Retrieve processingstatus item with given {processingstatusId}

        ``GET /coursereserves/processingstatuses/{status_id}``

        Args:
            status_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_processingstatus_return.schema 
        """
        return self.call("GET", f"/coursereserves/processingstatuses/{status_id}")

    def delete_processingstatus(self, status_id: str):
        """Delete processingstatus item with given {processingstatusId}

        ``DELETE /coursereserves/processingstatuses/{status_id}``

        Args:
            status_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/processingstatuses/{status_id}")

    def modify_processingstatus(self, status_id: str, processingstatus: dict):
        """Update a status by id

        ``PUT /coursereserves/processingstatuses/{status_id}``

        Args:
            status_id (str)
            processingstatus (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_processingstatus_request.schema
        """
        return self.call("PUT", f"/coursereserves/processingstatuses/{status_id}", data=processingstatus)

    def get_copyrightstatuses(self, **kwargs):
        """Return a list of copyright statuses

        ``GET /coursereserves/copyrightstatuses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    With valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_copyrightstatuses_return.schema 
        """
        return self.call("GET", "/coursereserves/copyrightstatuses", query=kwargs)

    def set_copyrightstatus(self, copyrightstatus: dict):
        """Create a new copyright status

        ``POST /coursereserves/copyrightstatuses``

        Args:
            copyrightstatus (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created copyrightstatus item

        Schema:

            .. literalinclude:: ../files/Courses_set_copyrightstatus_request.schema
        """
        return self.call("POST", "/coursereserves/copyrightstatuses", data=copyrightstatus)

    def delete_copyrightstatuses(self):
        """

        ``DELETE /coursereserves/copyrightstatuses``
        """
        return self.call("DELETE", "/coursereserves/copyrightstatuses")

    def get_copyrightstatus(self, status_id: str):
        """Retrieve copyrightstatus item with given {copyrightstatusId}

        ``GET /coursereserves/copyrightstatuses/{status_id}``

        Args:
            status_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_copyrightstatus_return.schema 
        """
        return self.call("GET", f"/coursereserves/copyrightstatuses/{status_id}")

    def delete_copyrightstatus(self, status_id: str):
        """Delete copyrightstatus item with given {copyrightstatusId}

        ``DELETE /coursereserves/copyrightstatuses/{status_id}``

        Args:
            status_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/copyrightstatuses/{status_id}")

    def modify_copyrightstatus(self, status_id: str, copyrightstatus: dict):
        """Update a status by id

        ``PUT /coursereserves/copyrightstatuses/{status_id}``

        Args:
            status_id (str)
            copyrightstatus (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_copyrightstatus_request.schema
        """
        return self.call("PUT", f"/coursereserves/copyrightstatuses/{status_id}", data=copyrightstatus)

    def get_courses_for_listing(self, listing_id: str, **kwargs):
        """Return a list of courses

        ``GET /coursereserves/courselistings/{listing_id}/courses``

        Args:
            listing_id (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_courses_for_listing_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/courses", query=kwargs)

    def get_courses(self, **kwargs):
        """Return a list of courses

        ``GET /coursereserves/courses``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_courses_return.schema 
        """
        return self.call("GET", "/coursereserves/courses", query=kwargs)

    def set_course_for_listing(self, listing_id: str, course: dict):
        """Create a new course

        ``POST /coursereserves/courselistings/{listing_id}/courses``

        Args:
            listing_id (str)
            course (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created course item

        Schema:

            .. literalinclude:: ../files/Courses_set_course_for_listing_request.schema
        """
        return self.call("POST", f"/coursereserves/courselistings/{listing_id}/courses", data=course)

    def set_course(self, course: dict):
        """Create a new course

        ``POST /coursereserves/courses``

        Args:
            course (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created course item

        Schema:

            .. literalinclude:: ../files/Courses_set_course_request.schema
        """
        return self.call("POST", "/coursereserves/courses", data=course)

    def delete_courses_for_listing(self, listing_id: str):
        """

        ``DELETE /coursereserves/courselistings/{listing_id}/courses``

        Args:
            listing_id (str)
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/courses")

    def delete_courses(self):
        """

        ``DELETE /coursereserves/courses``
        """
        return self.call("DELETE", "/coursereserves/courses")

    def get_course_for_listing(self, listing_id: str, course_id: str):
        """Retrieve course item with given {courseId}

        ``GET /coursereserves/courselistings/{listing_id}/courses/{course_id}``

        Args:
            listing_id (str)
            course_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_course_for_listing_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/courses/{course_id}")

    def get_course(self, course_id: str):
        """Retrieve course item with given {courseId}

        ``GET /coursereserves/courses/{course_id}``

        Args:
            course_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_course_return.schema 
        """
        return self.call("GET", f"/coursereserves/courses/{course_id}")

    def delete_course_for_listing(self, listing_id: str, course_id: str):
        """Delete course item with given {courseId}

        ``DELETE /coursereserves/courselistings/{listing_id}/courses/{course_id}``

        Args:
            listing_id (str)
            course_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/courses/{course_id}")

    def delete_course(self, course_id: str):
        """Delete course item with given {courseId}

        ``DELETE /coursereserves/courses/{course_id}``

        Args:
            course_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/courses/{course_id}")

    def modify_course_for_listing(self, listing_id: str, course_id: str, course: dict):
        """Update a course by id

        ``PUT /coursereserves/courselistings/{listing_id}/courses/{course_id}``

        Args:
            listing_id (str)
            course_id (str)
            course (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_course_for_listing_request.schema
        """
        return self.call("PUT", f"/coursereserves/courselistings/{listing_id}/courses/{course_id}", data=course)

    def modify_course(self, course_id: str, course: dict):
        """Update a course by id

        ``PUT /coursereserves/courses/{course_id}``

        Args:
            course_id (str)
            course (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_course_request.schema
        """
        return self.call("PUT", f"/coursereserves/courses/{course_id}", data=course)

    def get_reserves_for_listing(self, listing_id: str, **kwargs):
        """Return a list of reserves

        ``GET /coursereserves/courselistings/{listing_id}/reserves``

        Args:
            listing_id (str)
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_reserves_for_listing_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/reserves", query=kwargs)

    def get_reserves(self, **kwargs):
        """Return a list of reserves

        ``GET /coursereserves/reserves``

        Args:
            **kwargs (properties): Keyword Arguments

        Keyword Args:
            query (str):  A query expressed as a CQL string
                    (see [dev.folio.org/reference/glossary#cql](https://dev.folio.org/reference/glossary#cql))
                    using valid searchable fields.
                    The first example below shows the general form of a full CQL query,
                    but those fields might not be relevant in this context.
                    
                    with valid searchable fields
                    
                    
                    Example:
                    
                     - (username=="ab*" or personal.firstName=="ab*" or personal.lastName=="ab*") and active=="true" sortby personal.lastName personal.firstName barcode
                    
                     - name=aaa
            offset (int): (default=0) Skip over a number of elements by specifying an offset value for the query
                    
                    Example:
                    
                     - 0
            limit (int): (default=10) Limit the number of elements returned in the response
                    
                    Example:
                    
                     - 10

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_reserves_return.schema 
        """
        return self.call("GET", "/coursereserves/reserves", query=kwargs)

    def set_reserf_for_listing(self, listing_id: str, reserf: dict):
        """Create a new reserve

        ``POST /coursereserves/courselistings/{listing_id}/reserves``

        Args:
            listing_id (str)
            reserf (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created reserf item

        Schema:

            .. literalinclude:: ../files/Courses_set_reserf_for_listing_request.schema
        """
        return self.call("POST", f"/coursereserves/courselistings/{listing_id}/reserves", data=reserf)

    def set_reserf(self, reserf: dict):
        """Create a new reserve

        ``POST /coursereserves/reserves``

        Args:
            reserf (dict): See Schema below

        Raises:
            OkapiRequestError: Bad Request
            OkapiRequestUnauthorized: Authentication is required
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Headers:
            - **Location** - URI to the created reserf item

        Schema:

            .. literalinclude:: ../files/Courses_set_reserf_request.schema
        """
        return self.call("POST", "/coursereserves/reserves", data=reserf)

    def delete_reserves_for_listing(self, listing_id: str):
        """

        ``DELETE /coursereserves/courselistings/{listing_id}/reserves``

        Args:
            listing_id (str)
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/reserves")

    def delete_reserves(self):
        """

        ``DELETE /coursereserves/reserves``
        """
        return self.call("DELETE", "/coursereserves/reserves")

    def get_reserf_for_listing(self, listing_id: str, reserve_id: str):
        """Retrieve reserf item with given {reserfId}

        ``GET /coursereserves/courselistings/{listing_id}/reserves/{reserve_id}``

        Args:
            listing_id (str)
            reserve_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_reserf_for_listing_return.schema 
        """
        return self.call("GET", f"/coursereserves/courselistings/{listing_id}/reserves/{reserve_id}")

    def get_reserf(self, reserve_id: str):
        """Retrieve reserf item with given {reserfId}

        ``GET /coursereserves/reserves/{reserve_id}``

        Args:
            reserve_id (str)

        Returns:
            dict: See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiFatalError: Server Error

        Schema:

            .. literalinclude:: ../files/Courses_get_reserf_return.schema 
        """
        return self.call("GET", f"/coursereserves/reserves/{reserve_id}")

    def delete_reserf_for_listing(self, listing_id: str, reserve_id: str):
        """Delete reserf item with given {reserfId}

        ``DELETE /coursereserves/courselistings/{listing_id}/reserves/{reserve_id}``

        Args:
            listing_id (str)
            reserve_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/courselistings/{listing_id}/reserves/{reserve_id}")

    def delete_reserf(self, reserve_id: str):
        """Delete reserf item with given {reserfId}

        ``DELETE /coursereserves/reserves/{reserve_id}``

        Args:
            reserve_id (str)

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
        """
        return self.call("DELETE", f"/coursereserves/reserves/{reserve_id}")

    def modify_reserf_for_listing(self, listing_id: str, reserve_id: str, reserf: dict):
        """Update a reserve by id

        ``PUT /coursereserves/courselistings/{listing_id}/reserves/{reserve_id}``

        Args:
            listing_id (str)
            reserve_id (str)
            reserf (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_reserf_for_listing_request.schema
        """
        return self.call("PUT", f"/coursereserves/courselistings/{listing_id}/reserves/{reserve_id}", data=reserf)

    def modify_reserf(self, reserve_id: str, reserf: dict):
        """Update a reserve by id

        ``PUT /coursereserves/reserves/{reserve_id}``

        Args:
            reserve_id (str)
            reserf (dict): See Schema below

        Raises:
            OkapiRequestNotFound: Not Found
            OkapiRequestError: Bad Request
            OkapiFatalError: Server Error
            OkapiRequestUnprocessableEntity: Unprocessable Entity

        Schema:

            .. literalinclude:: ../files/Courses_modify_reserf_request.schema
        """
        return self.call("PUT", f"/coursereserves/reserves/{reserve_id}", data=reserf)
