import logging


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

main_logger = logging.getLogger("main")
main_logger.propagate = False
main_logger.setLevel(logging.WARN)

print(root_logger)
print(main_logger)