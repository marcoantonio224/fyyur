"""empty message

Revision ID: 94143c8196e6
Revises: 3e2be28fc9dd
Create Date: 2020-07-16 07:40:01.030441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94143c8196e6'
down_revision = '3e2be28fc9dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('image_link', sa.String(), nullable=True))
    op.add_column('shows', sa.Column('artist_image_link', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('image_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'image_link')
    op.drop_column('shows', 'artist_image_link')
    op.drop_column('artists', 'image_link')
    # ### end Alembic commands ###
