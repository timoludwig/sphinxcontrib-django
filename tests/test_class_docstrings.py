import pytest


@pytest.mark.sphinx("html", testroot="docstrings")
def test_simple_model(app, do_autodoc):
    actual = do_autodoc(app, "class", "dummy_django_app.models.SimpleModel")
    print(actual)
    assert actual == [
        "",
        ".. py:class:: SimpleModel(id, file, childA, dummy_field)",
        "   :module: dummy_django_app.models",
        "",
        "   :param id: Primary key: ID",
        "   :type id: ~django.db.models.AutoField",
        "   :param dummy_field: Very verbose name of dummy field. This should help you",
        "   :type dummy_field: ~django.db.models.CharField",
        "",
        "   Relationship fields:",
        "",
        "   :param file: File "
        "(related name: :attr:`~dummy_django_app.models.FileModel.simple_models`)",
        "   :type file: :class:`~django.db.models.ForeignKey` to "
        ":class:`~dummy_django_app.models.FileModel`",
        "   :param childA: ChildA "
        "(related name: :attr:`~dummy_django_app.models.ChildModelA.simple_model`)",
        "   :type childA: :class:`~django.db.models.OneToOneField` to "
        ":class:`~dummy_django_app.models.ChildModelA`",
        "   :param childrenB: ChildrenB "
        "(related name: :attr:`~dummy_django_app.models.ChildModelB.simple_models`)",
        "   :type childrenB: :class:`~django.db.models.ManyToManyField` to "
        ":class:`~dummy_django_app.models.ChildModelB`",
        "",
        "   Reverse relationships:",
        "",
        "   :param childmodela: All child model as of this simple model "
        "(related name of :attr:`~dummy_django_app.models.ChildModelA.simple_model`)",
        "   :type childmodela: Reverse :class:`~django.db.models.ForeignKey` from "
        ":class:`~dummy_django_app.models.ChildModelA`",
        "   :param childmodelb: All child model bs of this simple model "
        "(related name of :attr:`~dummy_django_app.models.ChildModelB.simple_model`)",
        "   :type childmodelb: Reverse :class:`~django.db.models.ForeignKey` from "
        ":class:`~dummy_django_app.models.ChildModelB`",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_abstract_model(app, do_autodoc):
    actual = do_autodoc(app, "class", "dummy_django_app.models.AbstractModel")
    print(actual)
    assert actual == [
        "",
        ".. py:class:: AbstractModel(*args, **kwargs)",
        "   :module: dummy_django_app.models",
        "",
        "",
        "   Relationship fields:",
        "",
        "   :param simple_model: Simple model "
        "(related name: :attr:`~dummy_django_app.models.SimpleModel.abstractmodel`)",
        "   :type simple_model: :class:`~django.db.models.ForeignKey` to :class:`~SimpleModel`",
        "   :param user: User (related name: :attr:`~django.contrib.auth.models.User.+`)",
        "   :type user: :class:`~django.db.models.ForeignKey` to :class:`~auth.User`",
        "   :param foreignkey_self: Foreignkey self "
        "(related name: :attr:`~dummy_django_app.models.AbstractModel.abstractmodel`)",
        "   :type foreignkey_self: :class:`~django.db.models.ForeignKey` to :class:`~self`",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_file_model(app, do_autodoc):
    actual = do_autodoc(app, "class", "dummy_django_app.models.FileModel")
    print(actual)
    assert actual == [
        "",
        ".. py:class:: FileModel(id, upload)",
        "   :module: dummy_django_app.models",
        "",
        "   :param id: Primary key: ID",
        "   :type id: ~django.db.models.AutoField",
        "   :param upload: Upload",
        "   :type upload: ~django.db.models.FileField",
        "",
        "   Reverse relationships:",
        "",
        "   :param simple_models: All simple models of this file model "
        "(related name of :attr:`~dummy_django_app.models.SimpleModel.file`)",
        "   :type simple_models: Reverse :class:`~django.db.models.ForeignKey` from "
        ":class:`~dummy_django_app.models.SimpleModel`",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_tagged_item(app, do_autodoc):
    actual = do_autodoc(app, "class", "dummy_django_app.models.TaggedItem")
    print(actual)
    assert actual == [
        "",
        ".. py:class:: TaggedItem(id, tag, content_type, object_id)",
        "   :module: dummy_django_app.models",
        "",
        "   :param id: Primary key: ID",
        "   :type id: ~django.db.models.AutoField",
        "   :param tag: Tag",
        "   :type tag: ~django.db.models.SlugField",
        "   :param object_id: Object id",
        "   :type object_id: ~django.db.models.PositiveIntegerField",
        "   :param content_object: Generic foreign key to the "
        ":class:`~django.contrib.contenttypes.models.ContentType` specified in "
        ":attr:`~dummy_django_app.models.TaggedItem.content_type`",
        "   :type content_object: ~django.contrib.contenttypes.fields.GenericForeignKey",
        "",
        "   Relationship fields:",
        "",
        "   :param content_type: Content type "
        "(related name: :attr:`~django.contrib.contenttypes.models.ContentType.taggeditem`)",
        "   :type content_type: :class:`~django.db.models.ForeignKey` to "
        ":class:`~django.contrib.contenttypes.models.ContentType`",
        "",
    ]


@pytest.mark.sphinx("html", testroot="docstrings")
def test_form(app, do_autodoc):
    actual = do_autodoc(app, "class", "dummy_django_app.forms.SimpleForm")
    print(actual)
    assert actual == [
        "",
        ".. py:class:: SimpleForm(*args, **kwargs)",
        "   :module: dummy_django_app.forms",
        "",
        "   **Form fields:**",
        "",
        "   * ``file``: File (:class:`~django.forms.ModelChoiceField`)",
        "   * ``childA``: ChildA (:class:`~django.forms.ModelChoiceField`)",
        "   * ``childrenB``: ChildrenB (:class:`~django.forms.ModelMultipleChoiceField`)",
        "   * ``dummy_field``: Very verbose name of dummy field "
        "(:class:`~django.forms.CharField`)",
        "   * ``test1``: Test1 (:class:`~django.forms.CharField`)",
        "   * ``test2``: Test2 (:class:`~django.forms.CharField`)",
        "",
    ]
