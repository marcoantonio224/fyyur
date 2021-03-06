"""empty message

Revision ID: 5798d82d5fa5
Revises: 4d3ebb801a4b
Create Date: 2020-07-16 07:36:57.499549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5798d82d5fa5'
down_revision = '4d3ebb801a4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'image_link')
    op.drop_column('venues', 'image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('image_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('image_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
