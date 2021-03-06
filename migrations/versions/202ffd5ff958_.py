"""empty message

Revision ID: 202ffd5ff958
Revises: b6979ca198d2
Create Date: 2020-07-16 08:11:35.894593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202ffd5ff958'
down_revision = 'b6979ca198d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('image_link', sa.VARCHAR(), server_default=sa.text("'/static/img/default-venue.png'::character varying"), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
