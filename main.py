import sentry_sdk

sentry_sdk.init(
    dsn="https://77963079ab291778e2e5458ffd8058b8@o4511529696559104.ingest.us.sentry.io/4511529706061824",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

division_by_zero = 1 / 0