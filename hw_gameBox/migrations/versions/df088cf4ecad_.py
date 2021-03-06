"""empty message

Revision ID: df088cf4ecad
Revises: 
Create Date: 2018-11-03 15:53:24.723315

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'df088cf4ecad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clicknumber', sa.Column('clicks', sa.Integer(), nullable=True))
    op.add_column('clicknumber', sa.Column('name', sa.String(length=200), nullable=True))
    op.add_column('clicknumber', sa.Column('sortId', sa.Integer(), nullable=True))
    op.drop_column('clicknumber', 'appid')
    op.drop_column('clicknumber', 'ClickNumbers')
    op.drop_column('clicknumber', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clicknumber', sa.Column('title', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('clicknumber', sa.Column('ClickNumbers', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('clicknumber', sa.Column('appid', mysql.VARCHAR(length=150), nullable=True))
    op.drop_column('clicknumber', 'sortId')
    op.drop_column('clicknumber', 'name')
    op.drop_column('clicknumber', 'clicks')
    # ### end Alembic commands ###
