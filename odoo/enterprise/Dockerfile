# syntax=devthefuture/dockerfile-x
# syntax=docker/dockerfile:experimental

# Extend the original Dockerfile
FROM ./odoo/Dockerfile

# Switch to root user
USER root

#--------------------------------------------#
#    Odoo Enterprise                         #
#--------------------------------------------#
# Extract the addons from the archives

RUN --mount=type=bind,src=./odoo/enterprise/source_archives,target=/tmp/enterprise_source_archives \
    if ! find /tmp/enterprise_source_archives -name "*.tar.gz" -print0 -quit | grep -q .; then \
        echo "No .tar.gz files found in ./odoo/enterprise/source_archives, expect Community version."; \
    else \
        echo "Extracting addons from .tar.gz files in ./odoo/enterprise/source_archives..., expect Enterprise version."; \
        find /tmp/enterprise_source_archives -name "*.tar.gz" -print0 -quit | while IFS= read -r -d $'\0' archive; do \
            archive_name=$(basename "$archive" .tar.gz); \
            mkdir -p "/tmp/${archive_name}"; \
            tar -xzf "$archive" -C "/tmp/${archive_name}"; \
            odoo_tag_major=$(echo "$ODOO_TAG" | cut -d '.' -f 1); \
            unlimited_dir=$(find "/tmp/${archive_name}" -type d -path "*/odoo${odoo_tag_major}_unlimited/odoo_unlimited" -print -quit); \
            if [ -n "$unlimited_dir" ]; then \
                echo "Relocating activation module..."; \
                mkdir -p "${THIRD_PARTY_ADDONS}"; \
                mv "$unlimited_dir" "${THIRD_PARTY_ADDONS}/"; \
                rm -rf "$(dirname "$unlimited_dir")"; \
            fi; \
            mkdir -p "${ENTERPRISE_ADDONS}"; \
            addons_path=$(find "/tmp/${archive_name}" -type d -path "*/odoo/addons" -print -quit); \
            if [ -n "$addons_path" ]; then \
                mv "${addons_path}/"* "${ENTERPRISE_ADDONS}/"; \
            fi; \
            rm -rf "/tmp/${archive_name}"; \
        done; \
    fi;

# Switch back to odoo user
USER odoo