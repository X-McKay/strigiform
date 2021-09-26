"""Functionality to use Hashicorp Vault to manage secrets."""
from os import getenv

import hvac

vault_url = getenv("VAULT_ADDR")
vault_token = getenv("VAULT_TOKEN")


class Vault:
    """Vault class to connect to vault and get/set keys."""

    def __init__(
        self,
        url: str = vault_url,
        token: str = vault_token,
        mount_point: str = "kv",
        path: str = "ibyrd",
    ):
        """Initialize Vault for storing secrets.

        :param url: Vault URL, defaults to getenv("VAULT_ADDR")
        :type url: str, optional
        :param token: Vault token for auth, defaults to getenv("VAULT_TOKEN")
        :type token: str, optional
        :param mount_point: Vault naming spec., defaults to "kv"
        :type mount_point: str, optional
        :param path: Vault path, defaults to "ibyrd"
        :type path: str, optional
        """
        self.url = url
        self.token = token
        self.mount_point = mount_point
        self.path = path

    def auth(self):
        """Connect to Vault client and verify auth.

        :return: Indicator if authentication occurred
        :rtype: bool
        """
        self.client = hvac.Client(self.url)
        return self.client.is_authenticated()

    def read_kv_secrets(self, v: int = 1):
        """Read key value pair secrets from vault.

        :param v: Version of kv pair to read, defaults to 1
        :type v: int, optional
        :return: KV secrets stored in vault
        :rtype: json
        """
        return self.client.secrets.kv.v2.read_secret_version(
            mount_point=self.mount_point, path=self.path, version=v
        )

    def create_or_update_kv(self, kv_dict: dict):
        """Create or update KV secrets in vault.

        :param kv_dict: Dictionary of key and value
        :type kv_dict: dict
        """
        self.client.secrets.kv.v2.create_or_update_secret(
            mount_point=self.mount_point, path=self.path, secret=kv_dict
        )

    def get_ebird_key(self, v: int = 1):
        """Retreive ebird API key from Vault.

        :param v: Version
        :type v: string
        """
        kv_secrets = self.read_kv_secrets(v)
        self.ebird_key = kv_secrets["data"]["data"]["EBIRD_KEY"]

    def set_ebird_key(self, value: str):
        """Set value of EBird API Key.

        :param value: New API key
        :type value: str
        """
        kv_dict = dict(EBIRD_KEY=value)
        self.create_or_update_kv(kv_dict=kv_dict)
