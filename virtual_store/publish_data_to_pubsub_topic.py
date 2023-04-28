import os, json, time
from google.cloud import pubsub_v1
from google.oauth2 import service_account


# This function is called by our virtual store app to push data into pub/sub topic
# before it gets pulled by the pub/sub subscriber
def pushData(eventData):
    projectid = "YOUR-PROJECT-ID"
    pubsub_topic = "projects/YOUR-PROJECT-ID/topics/YOUR-TOPIC-NAME"
    service_account_path = "YOUR-SERVICE-ACCOUNT-PATH"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

    publisher = pubsub_v1.PublisherClient.from_service_account_file(
        service_account_path
    )

    publisher.publish(pubsub_topic, eventData)


if __name__ == "__main__":
    testdata = str(
        {
            "order_id": "84c538fa-ef6f-11ea-a9c3-3db3abcedca9",
            "timestamp": 1599307283.61477,
            "ordered_item": [
                {
                    "item_name": "Trolly",
                    "item_id": "1001",
                    "category_name": "sample category 1",
                    "item_price": 200.00,
                    "item_qty": 6,
                },
                {
                    "item_name": "Mystery Box",
                    "item_id": "1002",
                    "category_name": "sample category 2",
                    "item_price": 125.00,
                    "item_qty": 9,
                },
                {
                    "item_name": "Gift Bag",
                    "item_id": "1003",
                    "category_name": "sample category 3",
                    "item_price": 50.90,
                    "item_qty": 1,
                },
                {
                    "item_name": "Small Block",
                    "item_id": "1004",
                    "category_name": "sample category 4",
                    "item_price": 12.00,
                    "item_qty": 12,
                },
                {
                    "item_name": "Cardboard Box",
                    "item_id": "1005",
                    "category_name": "sample category 5",
                    "item_price": 89.00,
                    "item_qty": 5,
                },
            ],
        }
    )
    testdata = json.dumps(testdata).encode("utf-8")
    pushData(testdata)
