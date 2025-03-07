"""rename address

Revision ID: 4c972b5a606f
Revises: b8d0767ba78f
Create Date: 2025-01-19 08:49:40.831500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c972b5a606f'
down_revision = 'b8d0767ba78f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',
               new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',
               new_column_name='address')
    # ### end Alembic commands ###
