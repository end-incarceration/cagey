from cagey import models
from slick import item, model, parser

PersonItem = model.realize_item_class('PersonItem', models.Person)
CaseItem = model.realize_item_class('CaseItem', models.Case)
BookingItem = model.realize_item_class('BookingItem', models.Booking)
ArrestItem = model.realize_item_class('ArrestItem', models.Arrest)
ChargeItem = model.realize_item_class('ChargeItem', models.Charge)
WarrantItem = model.realize_item_class('WarrantItem', models.Warrant)
BondItem = model.realize_item_class('BondItem', models.Bond)
