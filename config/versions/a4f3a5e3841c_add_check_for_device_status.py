"""add check for device status

Revision ID: a4f3a5e3841c
Revises: 978cb510fe7c
Create Date: 2024-12-30 11:45:58.481250

"""

# revision identifiers, used by Alembic.
revision = 'a4f3a5e3841c'
down_revision = '978cb510fe7c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('ps_endpoints', sa.Column('is_device_available', sa.Boolean(), default=False))
    op.create_index('ps_endpoints_is_device_available', 'ps_endpoints', ['is_device_available'])
    op.create_index('ps_endpoints_is_device_available_and_is_not_web', 'ps_endpoints', ['is_device_available', 'is_webuser'])



def downgrade():
    op.drop_column('ps_endpoints', 'is_device_available')

