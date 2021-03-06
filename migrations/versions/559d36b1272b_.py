"""empty message

Revision ID: 559d36b1272b
Revises: 58536606e54c
Create Date: 2020-07-16 08:16:38.604427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559d36b1272b'
down_revision = '58536606e54c'
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
