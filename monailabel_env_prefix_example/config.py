# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from importlib.metadata import distributions
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def is_package_installed(name: str) -> bool:
    return name in (x.metadata.get("Name") for x in distributions())


class Settings(BaseSettings):
    # ---- General ----
    API_STR: str = ""
    PROJECT_NAME: str = "MONAILabel"

    APP_DIR: str = ""
    STUDIES: str = ""
    APP_CONF: Dict[str, Any] = {}

    # ---- Auth ----
    AUTH_ENABLE: bool = False
    AUTH_REALM_URI: str = "http://localhost:8080/realms/monailabel"
    AUTH_TIMEOUT: int = 10
    AUTH_TOKEN_USERNAME: str = "preferred_username"
    AUTH_TOKEN_EMAIL: str = "email"
    AUTH_TOKEN_NAME: str = "name"
    AUTH_TOKEN_ROLES: str = "realm_access#roles"
    AUTH_CLIENT_ID: str = "monailabel-app"

    AUTH_ROLE_ADMIN: str = "monailabel-admin"
    AUTH_ROLE_REVIEWER: str = "monailabel-reviewer"
    AUTH_ROLE_ANNOTATOR: str = "monailabel-annotator"
    AUTH_ROLE_USER: str = "monailabel-user"

    # ---- Tasks ----
    TASKS_TRAIN: bool = True
    TASKS_STRATEGY: bool = True
    TASKS_SCORING: bool = True
    TASKS_BATCH_INFER: bool = True

    # ---- Datastore ----
    DATASTORE: str = ""
    DATASTORE_URL: str = ""
    DATASTORE_USERNAME: str = ""
    DATASTORE_PASSWORD: str = ""
    DATASTORE_API_KEY: str = ""
    DATASTORE_CACHE_PATH: str = ""
    DATASTORE_PROJECT: str = ""
    DATASTORE_ASSET_PATH: str = ""

    DATASTORE_DSA_ANNOTATION_GROUPS: str = ""

    # ---- DICOMweb (legacy compatibility retained) ----
    DICOMWEB_USERNAME: str = ""  # deprecated; use DATASTORE_USERNAME
    DICOMWEB_PASSWORD: str = ""  # deprecated; use DATASTORE_PASSWORD
    DICOMWEB_CACHE_PATH: str = ""  # deprecated; use DATASTORE_CACHE_PATH
    QIDO_PREFIX: Optional[str] = None
    WADO_PREFIX: Optional[str] = None
    STOW_PREFIX: Optional[str] = None
    DICOMWEB_FETCH_BY_FRAME: bool = False
    DICOMWEB_CONVERT_TO_NIFTI: bool = True
    DICOMWEB_SEARCH_FILTER: Dict[str, Any] = {"Modality": "CT"}
    DICOMWEB_CACHE_EXPIRY: int = 7200
    DICOMWEB_PROXY_TIMEOUT: float = 30.0
    DICOMWEB_READ_TIMEOUT: float = 5.0

    DATASTORE_AUTO_RELOAD: bool = True
    DATASTORE_READ_ONLY: bool = False
    DATASTORE_FILE_EXT: List[str] = [
        "*.nii.gz",
        "*.nii",
        "*.nrrd",
        "*.jpg",
        "*.png",
        "*.tif",
        "*.svs",
        "*.xml",
    ]

    # ---- Server / CORS ----
    SERVER_PORT: int = 8000
    CORS_ORIGINS: List[AnyHttpUrl] = []

    AUTO_UPDATE_SCORING: bool = True

    # ---- Sessions ----
    SESSIONS: bool = True
    SESSION_PATH: str = ""
    SESSION_EXPIRY: int = 3600

    # ---- Inference / Tracking ----
    INFER_CONCURRENCY: int = -1
    INFER_TIMEOUT: int = 600
    TRACKING_ENABLED: bool = True
    TRACKING_URI: str = ""

    # ---- MONAI Zoo (note: env vars are NOT prefixed with MONAI_LABEL_) ----
    MONAI_ZOO_SOURCE: str = Field(
        default_factory=lambda: os.environ.get("BUNDLE_DOWNLOAD_SRC", "monaihosting"),
        validation_alias="MONAI_ZOO_SOURCE",
    )
    MONAI_ZOO_REPO: str = Field(
        default="Project-MONAI/model-zoo/hosting_storage_v1",
        validation_alias="MONAI_ZOO_REPO",
    )
    MONAI_ZOO_AUTH_TOKEN: str = Field(
        default="", validation_alias="MONAI_ZOO_AUTH_TOKEN"
    )

    # ---- SAM model URLs depend on package presence ----
    SAM_MODEL_PT: str = (
        "https://huggingface.co/facebook/sam2.1-hiera-large/resolve/main/sam2.1_hiera_large.pt"
        if is_package_installed("SAM-2")
        else "https://huggingface.co/facebook/sam2-hiera-large/resolve/main/sam2_hiera_large.pt"
    )
    SAM_MODEL_CFG: str = (
        "https://huggingface.co/facebook/sam2.1-hiera-large/resolve/main/sam2.1_hiera_l.yaml"
        if is_package_installed("SAM-2")
        else "https://huggingface.co/facebook/sam2-hiera-large/resolve/main/sam2_hiera_l.yaml"
    )

    # Prefer settings parsing for this (bool env like MONAI_LABEL_USE_ITK_FOR_DICOM_SEG=true/false)
    USE_ITK_FOR_DICOM_SEG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
        env_prefix="MONAI_LABEL_",  # <<< key line: map fields to MONAI_LABEL_* env vars
    )


settings = Settings()

RBAC_ADMIN = f"|RBAC: {settings.AUTH_ROLE_ADMIN}| - " if settings.AUTH_ENABLE else ""
RBAC_REVIEWER = (
    f"|RBAC: {settings.AUTH_ROLE_REVIEWER}| - " if settings.AUTH_ENABLE else ""
)
RBAC_ANNOTATOR = (
    f"|RBAC: {settings.AUTH_ROLE_ANNOTATOR}| - " if settings.AUTH_ENABLE else ""
)
RBAC_USER = f"|RBAC: {settings.AUTH_ROLE_USER}| - " if settings.AUTH_ENABLE else ""
