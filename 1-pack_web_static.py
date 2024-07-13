from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Create a .tgz archive from web_static folder.
    """
    # Define paths
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_file = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join('versions', archive_file)
    web_static_path = 'web_static'

    # Create versions directory if it doesn't exist
    c.run('mkdir -p versions')

    # Compress web_static folder into a .tgz archive
    result = c.local(f'tar -cvzf {archive_path} {web_static_path}')

    # Check if the archive was created successfully
    if result.failed:
        return None
    else:
        return archive_path
