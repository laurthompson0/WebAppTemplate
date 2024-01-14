FROM nginx

# remove the default html pages, add dir for templates
RUN rm -rf /usr/share/nginx/html/* && mkdir -p /etc/nginx/templates

COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/default.conf /etc/nginx/templates/default.conf.templates