"""empty message

Revision ID: 3b465be0e664
Revises: None
Create Date: 2015-08-03 09:08:00.528064

"""

# revision identifiers, used by Alembic.
revision = '3b465be0e664'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donorinfo', sa.Column('donor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'donorinfo', 'donors', ['donor_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'donorinfo', type_='foreignkey')
    op.drop_column('donorinfo', 'donor_id')
    ### end Alembic commands ###