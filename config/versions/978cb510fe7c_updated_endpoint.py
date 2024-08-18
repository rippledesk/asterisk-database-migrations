"""updated endpoint

Revision ID: 978cb510fe7c
Revises: 6c475a93f48a
Create Date: 2024-08-18 12:06:06.033431

"""

# revision identifiers, used by Alembic.
revision = '978cb510fe7c'
down_revision = '6c475a93f48a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ps_endpoints', sa.Column('password_for_router', sa.String(255)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.drop_column('ps_endpoints', 'password_for_router')
    # ### end Alembic commands ###
