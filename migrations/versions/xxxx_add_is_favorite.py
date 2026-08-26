"""add is_favorite

Revision ID: xxxx_add_is_favorite
Revises: None
Create Date: 2023-10-27 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx_add_is_favorite'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add 'is_favorite' column to 'bookmark' table with a default value of False
    op.add_column('bookmark', sa.Column('is_favorite', sa.Boolean(), nullable=False, server_default=sa.text('0')))


def downgrade():
    # Remove 'is_favorite' column from 'bookmark' table
    op.drop_column('bookmark', 'is_favorite')
