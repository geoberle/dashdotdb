"""empty message

Revision ID: 3f43e3d39346
Revises: b22e5138a938
Create Date: 2021-03-17 22:59:29.105121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f43e3d39346'
down_revision = 'b22e5138a938'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('slitype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('serviceslo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.Column('slitype_id', sa.Integer(), nullable=True),
    sa.Column('token_id', sa.Integer(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=True),
    sa.Column('namespace_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cluster_id'], ['cluster.id'], ),
    sa.ForeignKeyConstraint(['namespace_id'], ['namespace.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['slitype_id'], ['slitype.id'], ),
    sa.ForeignKeyConstraint(['token_id'], ['token.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('serviceslo')
    op.drop_table('slitype')
    op.drop_table('service')
    # ### end Alembic commands ###