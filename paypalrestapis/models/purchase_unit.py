# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.amount_with_breakdown import AmountWithBreakdown
from paypalrestapis.models.item import Item
from paypalrestapis.models.payee import Payee
from paypalrestapis.models.payment_collection import PaymentCollection
from paypalrestapis.models.payment_instruction import PaymentInstruction
from paypalrestapis.models.shipping_with_tracking_details import ShippingWithTrackingDetails
from paypalrestapis.models.supplementary_data import SupplementaryData


class PurchaseUnit(object):

    """Implementation of the 'Purchase Unit' model.

    The purchase unit details. Used to capture required information for the
    payment contract.

    Attributes:
        reference_id (str): The API caller-provided external ID for the
            purchase unit. Required for multiple purchase units when you must
            update the order through `PATCH`. If you omit this value and the
            order contains only one purchase unit, PayPal sets this value to
            `default`. <blockquote><strong>Note:</strong> If there are
            multiple purchase units, <code>reference_id</code> is required for
            each purchase unit.</blockquote>
        amount (AmountWithBreakdown): The total order amount with an optional
            breakdown that provides details, such as the total item amount,
            total tax amount, shipping, handling, insurance, and discounts, if
            any.<br/>If you specify `amount.breakdown`, the amount equals
            `item_total` plus `tax_total` plus `shipping` plus `handling` plus
            `insurance` minus `shipping_discount` minus discount.<br/>The
            amount must be a positive number. For listed of supported
            currencies and decimal precision, see the PayPal REST APIs <a
            href="/docs/integration/direct/rest/currency-codes/">Currency
            Codes</a>.
        payee (Payee): The merchant who receives the funds and fulfills the
            order. The merchant is also known as the payee.
        payment_instruction (PaymentInstruction): Any additional payment
            instructions to be consider during payment processing. This
            processing instruction is applicable for Capturing an order or
            Authorizing an Order.
        description (str): The purchase description.
        custom_id (str): The API caller-provided external ID. Used to
            reconcile API caller-initiated transactions with PayPal
            transactions. Appears in transaction and settlement reports.
        invoice_id (str): The API caller-provided external invoice ID for this
            order.
        id (str): The PayPal-generated ID for the purchase unit. This ID
            appears in both the payer's transaction history and the emails
            that the payer receives. In addition, this ID is available in
            transaction and settlement reports that merchants and API callers
            can use to reconcile transactions. This ID is only available when
            an order is saved by calling
            <code>v2/checkout/orders/id/save</code>.
        soft_descriptor (str): The payment descriptor on account transactions
            on the customer's credit card statement, that PayPal sends to
            processors. The maximum length of the soft descriptor information
            that you can pass in the API field is 22 characters, in the
            following format:<code>22 - len(PAYPAL * (8)) -
            len(<var>Descriptor in Payment Receiving Preferences of Merchant
            account</var> + 1)</code>The PAYPAL prefix uses 8
            characters.<br/><br/>The soft descriptor supports the following
            ASCII characters:<ul><li>Alphanumeric
            characters</li><li>Dashes</li><li>Asterisks</li><li>Periods
            (.)</li><li>Spaces</li></ul>For Wallet payments marketplace
            integrations:<ul><li>The merchant descriptor in the Payment
            Receiving Preferences must be the marketplace name.</li><li>You
            can't use the remaining space to show the customer service
            number.</li><li>The remaining spaces can be a combination of
            seller name and country.</li></ul><br/>For unbranded payments
            (Direct Card) marketplace integrations, use a combination of the
            seller name and phone number.
        items (List[Item]): An array of items that the customer purchases from
            the merchant.
        shipping (ShippingWithTrackingDetails): The order shipping details.
        supplementary_data (SupplementaryData): Supplementary data about a
            payment. This object passes information that can be used to
            improve risk assessments and processing costs, for example, by
            providing Level 2 and Level 3 payment data.
        payments (PaymentCollection): The collection of payments, or
            transactions, for a purchase unit in an order. For example,
            authorized payments, captured payments, and refunds.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reference_id": 'reference_id',
        "amount": 'amount',
        "payee": 'payee',
        "payment_instruction": 'payment_instruction',
        "description": 'description',
        "custom_id": 'custom_id',
        "invoice_id": 'invoice_id',
        "id": 'id',
        "soft_descriptor": 'soft_descriptor',
        "items": 'items',
        "shipping": 'shipping',
        "supplementary_data": 'supplementary_data',
        "payments": 'payments'
    }

    _optionals = [
        'reference_id',
        'amount',
        'payee',
        'payment_instruction',
        'description',
        'custom_id',
        'invoice_id',
        'id',
        'soft_descriptor',
        'items',
        'shipping',
        'supplementary_data',
        'payments',
    ]

    def __init__(self,
                 reference_id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 payee=APIHelper.SKIP,
                 payment_instruction=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 custom_id=APIHelper.SKIP,
                 invoice_id=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 soft_descriptor=APIHelper.SKIP,
                 items=APIHelper.SKIP,
                 shipping=APIHelper.SKIP,
                 supplementary_data=APIHelper.SKIP,
                 payments=APIHelper.SKIP):
        """Constructor for the PurchaseUnit class"""

        # Initialize members of the class
        if reference_id is not APIHelper.SKIP:
            self.reference_id = reference_id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if payee is not APIHelper.SKIP:
            self.payee = payee 
        if payment_instruction is not APIHelper.SKIP:
            self.payment_instruction = payment_instruction 
        if description is not APIHelper.SKIP:
            self.description = description 
        if custom_id is not APIHelper.SKIP:
            self.custom_id = custom_id 
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if id is not APIHelper.SKIP:
            self.id = id 
        if soft_descriptor is not APIHelper.SKIP:
            self.soft_descriptor = soft_descriptor 
        if items is not APIHelper.SKIP:
            self.items = items 
        if shipping is not APIHelper.SKIP:
            self.shipping = shipping 
        if supplementary_data is not APIHelper.SKIP:
            self.supplementary_data = supplementary_data 
        if payments is not APIHelper.SKIP:
            self.payments = payments 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        reference_id = dictionary.get("reference_id") if dictionary.get("reference_id") else APIHelper.SKIP
        amount = AmountWithBreakdown.from_dictionary(dictionary.get('amount')) if 'amount' in dictionary.keys() else APIHelper.SKIP
        payee = Payee.from_dictionary(dictionary.get('payee')) if 'payee' in dictionary.keys() else APIHelper.SKIP
        payment_instruction = PaymentInstruction.from_dictionary(dictionary.get('payment_instruction')) if 'payment_instruction' in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        custom_id = dictionary.get("custom_id") if dictionary.get("custom_id") else APIHelper.SKIP
        invoice_id = dictionary.get("invoice_id") if dictionary.get("invoice_id") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        soft_descriptor = dictionary.get("soft_descriptor") if dictionary.get("soft_descriptor") else APIHelper.SKIP
        items = None
        if dictionary.get('items') is not None:
            items = [Item.from_dictionary(x) for x in dictionary.get('items')]
        else:
            items = APIHelper.SKIP
        shipping = ShippingWithTrackingDetails.from_dictionary(dictionary.get('shipping')) if 'shipping' in dictionary.keys() else APIHelper.SKIP
        supplementary_data = SupplementaryData.from_dictionary(dictionary.get('supplementary_data')) if 'supplementary_data' in dictionary.keys() else APIHelper.SKIP
        payments = PaymentCollection.from_dictionary(dictionary.get('payments')) if 'payments' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(reference_id,
                   amount,
                   payee,
                   payment_instruction,
                   description,
                   custom_id,
                   invoice_id,
                   id,
                   soft_descriptor,
                   items,
                   shipping,
                   supplementary_data,
                   payments)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'reference_id={(self.reference_id if hasattr(self, "reference_id") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'payee={(self.payee if hasattr(self, "payee") else None)!r}, '
                f'payment_instruction={(self.payment_instruction if hasattr(self, "payment_instruction") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'custom_id={(self.custom_id if hasattr(self, "custom_id") else None)!r}, '
                f'invoice_id={(self.invoice_id if hasattr(self, "invoice_id") else None)!r}, '
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'soft_descriptor={(self.soft_descriptor if hasattr(self, "soft_descriptor") else None)!r}, '
                f'items={(self.items if hasattr(self, "items") else None)!r}, '
                f'shipping={(self.shipping if hasattr(self, "shipping") else None)!r}, '
                f'supplementary_data={(self.supplementary_data if hasattr(self, "supplementary_data") else None)!r}, '
                f'payments={(self.payments if hasattr(self, "payments") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'reference_id={(self.reference_id if hasattr(self, "reference_id") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'payee={(self.payee if hasattr(self, "payee") else None)!s}, '
                f'payment_instruction={(self.payment_instruction if hasattr(self, "payment_instruction") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'custom_id={(self.custom_id if hasattr(self, "custom_id") else None)!s}, '
                f'invoice_id={(self.invoice_id if hasattr(self, "invoice_id") else None)!s}, '
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'soft_descriptor={(self.soft_descriptor if hasattr(self, "soft_descriptor") else None)!s}, '
                f'items={(self.items if hasattr(self, "items") else None)!s}, '
                f'shipping={(self.shipping if hasattr(self, "shipping") else None)!s}, '
                f'supplementary_data={(self.supplementary_data if hasattr(self, "supplementary_data") else None)!s}, '
                f'payments={(self.payments if hasattr(self, "payments") else None)!s})')
