# Use the official httpd image from the Docker Hub
FROM httpd:latest

# Copy custom configuration file to the image
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

# Copy website content to the image
COPY ./public-html/ /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# Start the httpd server
CMD ["httpd-foreground"]