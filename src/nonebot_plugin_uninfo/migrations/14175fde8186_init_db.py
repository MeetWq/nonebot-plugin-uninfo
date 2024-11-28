"""init_db

迁移 ID: 14175fde8186
父迁移:
创建时间: 2024-10-30 16:27:05.032427

"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa

revision: str = "14175fde8186"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("nonebot_plugin_uninfo",)
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_uninfo_botmodel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("self_id", sa.String(length=64), nullable=False),
        sa.Column("adapter", sa.String(length=32), nullable=False),
        sa.Column("scope", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_uninfo_botmodel")),
        sa.UniqueConstraint("self_id", "adapter", name="unique_bot"),
        info={"bind_key": "nonebot_plugin_uninfo"},
    )
    op.create_table(
        "nonebot_plugin_uninfo_scenemodel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bot_persist_id", sa.Integer(), nullable=False),
        sa.Column("parent_scene_persist_id", sa.Integer(), nullable=True),
        sa.Column("scene_id", sa.String(length=64), nullable=False),
        sa.Column("scene_type", sa.Integer(), nullable=False),
        sa.Column("scene_data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_uninfo_scenemodel")),
        sa.UniqueConstraint("bot_persist_id", "scene_id", "scene_type", name="unique_scene"),
        info={"bind_key": "nonebot_plugin_uninfo"},
    )
    op.create_table(
        "nonebot_plugin_uninfo_usermodel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bot_persist_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(length=64), nullable=False),
        sa.Column("user_data", sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_uninfo_usermodel")),
        sa.UniqueConstraint("bot_persist_id", "user_id", name="unique_user"),
        info={"bind_key": "nonebot_plugin_uninfo"},
    )
    op.create_table(
        "nonebot_plugin_uninfo_sessionmodel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("bot_persist_id", sa.Integer(), nullable=False),
        sa.Column("scene_persist_id", sa.Integer(), nullable=False),
        sa.Column("user_persist_id", sa.Integer(), nullable=False),
        sa.Column("member_data", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_uninfo_sessionmodel")),
        sa.UniqueConstraint("bot_persist_id", "scene_persist_id", "user_persist_id", name="unique_session"),
        info={"bind_key": "nonebot_plugin_uninfo"},
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_uninfo_botmodel")
    op.drop_table("nonebot_plugin_uninfo_scenemodel")
    op.drop_table("nonebot_plugin_uninfo_usermodel")
    op.drop_table("nonebot_plugin_uninfo_sessionmodel")
    # ### end Alembic commands ###