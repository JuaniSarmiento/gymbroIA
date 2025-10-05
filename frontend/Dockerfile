# Fase 1: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Fase 2: Production
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/build ./build
# Usamos un servidor simple para producción
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]