from database import get_driver


def test_connection():
    driver = get_driver()

    try:
        driver.verify_connectivity()

        print("=" * 50)
        print("SUCCESS!")
        print("PatentGraph AI connected to CognoDB.")
        print("=" * 50)

    except Exception as error:
        print("=" * 50)
        print("CONNECTION FAILED")
        print("=" * 50)
        print(error)


if __name__ == "__main__":
    test_connection()