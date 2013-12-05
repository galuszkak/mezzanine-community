from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="Enable Twitter",
    label=_("For sending info about events"),
    description=_("For sending info about events."),
    editable=True,
    default=True,
)

register_setting(
    name="Consumer Key",
    label=_("Twitter Consumer Key"),
    description=_("Twitter Consumer Key"),
    editable=True,
    default="",
)

register_setting(
    name="Consumer Secret",
    label=_("Twitter Consumer Secret"),
    description=_("Twitter Consumer Secret."),
    editable=True,
    default="",
)

register_setting(
    name="Access Token",
    label=_("Twitter Access Token"),
    description=_("Twitter Access Token."),
    editable=True,
    default="",
)

register_setting(
    name="Access Token secret",
    label=_("Twitter Access Token secret"),
    description=_("Twitter Access Token secret."),
    editable=True,
    default="",
    )
register_setting(
    name="Enable LinkedIn",
    label=_("For sending info about events"),
    description=_("For sending info about events."),
    editable=True,
    default=True,
)

register_setting(
    name="Enable Facebook",
    label=_("For sending info about events"),
    description=_("For sending info about events."),
    editable=True,
    default=True,
)

register_setting(
    name="Facebook OAuth Token",
    label=_("Token for posting on pages"),
    description=_("Token for posting on pages"),
    editable=True,
    default="",
)

register_setting(
    name="Enable Google Plus",
    label=_("For sending info about events"),
    description=_("For sending info about events."),
    editable=True,
    default=True,
)

register_setting(
    name="Google Plus login",
    label=_("Google Plus login"),
    description=_("Google Plus login."),
    editable=True,
    default="",
)

register_setting(
    name="Google Plus password",
    label=_("Google Plus password"),
    description=_("Google Plus password"),
    editable=True,
    default="",
)
