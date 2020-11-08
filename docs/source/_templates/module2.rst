{{ fullname | escape | underline }}


.. automodule:: {{ fullname }}

    {% block attributes %}
    {% if attributes %}
    .. rubric:: Module Attributes

   .. autosummary::
      :toctree:
    {% endif %}
    {% endblock %}

    {% block classes %}
    {% if classes %}
    .. rubric:: {{ _('Classes') }}

    .. autosummary::
        :toctree:
        :template: class.rst
        {% for item in classes %}
            {{ item }}
        {%- endfor %}
    {% endif %}
    {% endblock %}
    
    
    {% block exceptions %}
    {% if exceptions %}
    .. rubric:: {{ _('Exceptions') }}

    .. autosummary::
    {% for item in exceptions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}


{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
    :template: module2.rst
    :recursive:

{% for item in modules %}
    {{ item }}

{%- endfor %}
{% endif %}
{% endblock %}