"""empty message

Revision ID: 5cc64b854c17
Revises: 
Create Date: 2024-08-11 22:32:25.407709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cc64b854c17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(length=160), nullable=False),
    sa.Column('user_name', sa.String(length=40), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('authorized_name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('wallet',
    sa.Column('id', sa.String(length=8), nullable=False),
    sa.Column('wallet_name', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('part',
    sa.Column('id', sa.String(length=8), nullable=False),
    sa.Column('part_name', sa.String(length=40), nullable=False),
    sa.Column('parent_wallet_id', sa.String(length=8), nullable=False),
    sa.ForeignKeyConstraint(['parent_wallet_id'], ['wallet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('part')
    op.drop_table('wallet')
    op.drop_table('user')
    # ### end Alembic commands ###
