"""empty message

Revision ID: 8f0753144ce7
Revises: 14ab9fb8f6f4
Create Date: 2020-07-16 08:20:41.447676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f0753144ce7'
down_revision = '14ab9fb8f6f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
