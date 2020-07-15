"""empty message

Revision ID: f434ffcb0f0d
Revises: f31952960ae0
Create Date: 2020-07-12 17:19:53.676104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f434ffcb0f0d'
down_revision = 'f31952960ae0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'venue_name')
    # ### end Alembic commands ###