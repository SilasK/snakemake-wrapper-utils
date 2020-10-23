def get_java_opts(snakemake):
    """Obtain java_opts from params, and handle resource definitions in resources."""

    java_opts = snakemake.params.get("java_opts", "")
    # Getting memory in megabytes, if java opts is not filled with -Xmx parameter
    # By doing so, backward compatibility is preserved
    if "mem_mb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
        java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

    # Getting memory in gigabytes, for user convenience. Please prefer the use
    # of mem_mb over mem_gb as advised in documentation.
    elif "mem_gb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
        java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

    # Getting java temp directory from output files list, if -Djava.io.tmpdir
    # is not provided in java parameters. By doing so, backward compatibility is
    # not broken.
    if "java_temp" in snakemake.output.keys() and not "-Djava.io.tmpdir" in java_opts:
        java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])

    return java_opts
