# -*- coding: utf-8 -*-

import settings
import signal

from contrib.node import get_spv_node
from contrib.restapp import get_app
from contrib.restapp import shutdown_handler


if __name__ == '__main__':
    spv = get_spv_node(settings)
    app = get_app()
    spv.start()
    app.run(debug=True,
            use_reloader=False,
            host=settings.WEB_HOST_IP,
            port=settings.WEB_HOST_PORT,
            threaded=False)
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.pause()
