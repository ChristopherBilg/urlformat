#include <regex.h>
#include <stdio.h>
#include <string.h>

#define LENGTH 2000
#define MAX_MATCHES 9

typedef struct {
  char url[LENGTH];
  char scheme[LENGTH];
  char authority[LENGTH];
  char path[LENGTH];
  char file[LENGTH];
  char query[LENGTH];
  char fragment[LENGTH];
  char username[LENGTH];
  char password[LENGTH];
  char hostname[LENGTH];
  char port[LENGTH];
} UrlParser;

UrlParser initilize(char url[LENGTH]) {
  UrlParser url_p;

  // UrlParser.url
  strcpy(url_p.url, url);

  // Return the UrlParser object
  return url_p;
}

int main() {
  UrlParser p = initilize("https://www.google.com");
  printf("%s\n", p.url);

  return 1;
}
