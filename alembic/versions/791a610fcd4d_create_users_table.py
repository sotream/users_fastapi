"""Create users table

Revision ID: 791a610fcd4d
Revises:
Create Date: 2024-06-22 21:08:24.916000

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func


# This is the revision identifier
revision = '791a610fcd4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add your upgrade instructions here
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP, server_default=func.now()),
    sa.Column('updated_at', sa.TIMESTAMP, server_default=func.now(), onupdate=func.now())
    )


def downgrade():
    # Add your downgrade instructions here
    op.drop_table('users')
