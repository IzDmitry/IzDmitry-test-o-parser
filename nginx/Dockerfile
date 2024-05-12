FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY static /home/app/web/staticfiles/

RUN chown -R nginx:nginx /home/app/web/staticfiles/
