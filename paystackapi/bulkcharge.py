"""Script used to define the paystack Charge class."""

from paystackapi.base import PayStackBase

class BulkCharge(PayStackBase):

    @classmethod
    def initiate_bulk_charge(cls, **kwargs):
        """
        Initiate a bulk charge.

        {
            "type": "array",
            "description": "",
            "format": ""
        }
        
        Args:
            authorization: Authorization token
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """

        return cls.requests.post("bulkcharge", data='kwargs')


    @classmethod
    def list_bulk_charge(cls, **kwargs):
        """

        Listall the  bulk charge batches created by the integration.

        Args:
            perPage: Number of transfers lsited per page for pagination
            page: number of pages listed by pagination.

            Returns:
            Json data from paystack API.

        """

        return cls.requests.get("bulkcharge", data="kwargs")



    @classmethod
    def fetch_bulk_charge(cls, **kwargs):
        """

        Fetch the charges associated with a specified batch code.

        Args:
            id_or_code: An ID or code for the batch whose charges you want to retrieve.
            perPage: Number of transfers lsited per page for pagination
            page: number of pages listed by pagination.


            Returns:
            Json data from paystack API.

        """

        return cls.requests.get("bulkcharge/{id_or_code}/charges", data="kwargs")

    
    @classmethod
    def pause_bulk_charge(cls, **kwargs):
        """
        Pause the proccessing of an ongoing bulk charge batch.

        Args:
            batch_code: code of the batch to be paused

        Returns:
        Json data from the Paystack API.

        """
        return cls.requests.get("bulkcharge/pause/{batch_code}", data="kwargs")

    
    @classmethod
    def resume_bulk_charge(cls, **kwargs):
        """
        Resume the proccessing of an already paused bulk charge batch.

        Args:
            batch_code: code of the batch to be resumed

        Returns:
        Json data from the Paystack API.

        """
        return cls.requests.get("bulkcharge/resume/{batch_code}", data="kwargs")


    


