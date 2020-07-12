"""empty message

Revision ID: 5f80be322142
Revises: 4d71f95cfe3c
Create Date: 2020-07-11 17:23:56.139649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f80be322142'
down_revision = '4d71f95cfe3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('image_link', sa.String(), nullable=False))
    op.add_column('venues', sa.Column('past_shows', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('upcoming_shows', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'upcoming_shows')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'past_shows')
    op.drop_column('venues', 'image_link')
    # ### end Alembic commands ###