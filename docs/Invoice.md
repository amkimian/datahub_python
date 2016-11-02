# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | The user this invoice relates to | [optional] 
**number** | **str** | The invoice id | [optional] 
**oneoff** | **bool** | Whether this is an out of cycle (not monthly) invoice | [optional] 
**invoice_date** | **date** | The date of this invoice | [optional] 
**year** | **int** |  | [optional] 
**month** | **int** | The month this invoice applies to (the cycle) | [optional] 
**status** | **str** | The status of this invoice (open, paid, cancelled) | [optional] 
**entries** | [**list[InvoiceEntry]**](InvoiceEntry.md) | The entries of this invoice | [optional] 
**subtotal** | **int** | Subtotal before tax in cents | [optional] 
**tax** | **int** | Any tax due on this invoice in cents | [optional] 
**total** | **int** | The total amount of the invoice (in cents in case the tax) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


