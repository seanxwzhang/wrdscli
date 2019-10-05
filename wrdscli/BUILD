package(default_visibility=["//visibility:public"])

py_library(
    name="common",
    srcs=[
        "common.py"
    ],
    data=glob(["config/**/*.ini"])
)

py_binary(
    name="wrdscli",
    srcs=[
        "wrdscli.py"
    ],
    deps=[
        "//db:db_commands"
    ]
)