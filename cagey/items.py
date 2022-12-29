from cagey import models
from cagey.slick import item, model, parser

PersonItem = model.realize_item_class('PersonItem', models.Person)
PersonItem._dedup_attribute = 'id'

CaseItem = model.realize_item_class('CaseItem', models.Case)
CaseItem._dedup_attribute = 'case_id'

BookingItem = model.realize_item_class('BookingItem', models.Booking)
BookingItem._dedup_attribute = 'id'

ArrestItem = model.realize_item_class('ArrestItem', models.Arrest)
ArrestItem._dedup_attribute = 'id'

ChargeItem = model.realize_item_class('ChargeItem', models.Charge)
ChargeItem._dedup_attribute = 'id'

WarrantItem = model.realize_item_class('WarrantItem', models.Warrant)
WarrantItem._dedup_attribute = 'id'

BondItem = model.realize_item_class('BondItem', models.Bond)
BondItem._dedup_attribute = 'id'
